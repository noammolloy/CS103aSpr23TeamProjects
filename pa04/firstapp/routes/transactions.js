/*
  todo.js -- Router for the ToDoList
*/
const express = require('express');
const router = express.Router();
const User = require('../models/User')
const TransactionItem = require('../models/TransactionItem')
const mongoose = require('mongoose')


/*
this is a very simple server which maintains a key/value
store using an object where the keys and values are lists of strings

*/

isLoggedIn = (req,res,next) => {
  if (res.locals.loggedIn) {
    next()
  } else {
    res.redirect('/login')
  }
}

// get the value associated to the key
router.get('/transactions/',
  isLoggedIn,
  async (req, res, next) => {
      const sort = req.query.sort
      let items = []
      if (sort=='category'){
        items = await TransactionItem.find({userId:req.user._id})
                                      .sort({category: 1})
      } else if (sort=='amount'){
        items = await TransactionItem.find({userId:req.user._id})
                                      .sort({amount: 1})
      } else if (sort=='description'){
        items = await TransactionItem.find({userId:req.user._id})
                                      .sort({description: 1})
      } else if (sort=='date'){
        items = await TransactionItem.find({userId:req.user._id})
                                      .sort({date: 1})
      } else {
        items = await TransactionItem.find({userId:req.user._id})
      }

      res.render('transactions', {items});
});

/* add the value in the body to the list associated to the key */
router.post('/transactions',
  isLoggedIn,
  async (req, res, next) => {
      const transaction = new TransactionItem(
        {description: req.body.desc,
         amount: req.body.amt,
         category: req.body.cat,
         date: req.body.date,
         userId: req.user._id
        })
      await transaction.save();
      res.redirect('/transactions')
});

router.get('/transactions/remove/:itemId',
  isLoggedIn,
  async (req, res, next) => {
      console.log("inside /transactions/remove/:itemId")
      await TransactionItem.deleteOne({_id:req.params.itemId});
      res.redirect('/transactions')
});

router.get('/transactions/edit/:itemId',
  isLoggedIn,
  async (req, res, next) => {
      console.log("inside /transactions/edit/:itemId")
      const item = 
       await TransactionItem.findById(req.params.itemId);
      // res.render('transactionEdit', { item });
      res.locals.item = item
      res.render('transactionEdit')
      //res.json(item)
});

router.post('/transactions/updateTransactionItem',
  isLoggedIn,
  async (req, res, next) => {
      const {itemId,description,amount,category,date} = req.body;
      await TransactionItem.findOneAndUpdate(
        {_id:itemId},
        {$set: {description,amount,category,date}} );
      res.redirect('/transactions')
});

router.get('/transactions/groupByCategory',
  isLoggedIn,
  async (req, res, next) => {
      let results = 
            await TransactionItem.aggregate([
                { $match: {
                  userId: new mongoose.Types.ObjectId(req.user._id)
                }},
                { $group: {
                  _id: '$category',
                  total: { $sum: '$amount' } // calculate the total amount for each category
                }},
                // { $sort: { total: -1 } } // sort the results by category
            ]);

        console.log('hi')
        console.log(results)
        res.render('categoryTable',{results})
});



module.exports = router;