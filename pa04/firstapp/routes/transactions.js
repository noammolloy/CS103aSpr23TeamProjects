/*
  todo.js -- Router for the ToDoList
*/
const express = require('express');
const router = express.Router();
const User = require('../models/User')
const TransactionItem = require('../models/TransactionItem')


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
      let items = await TransactionItem.find({userId:req.user._id})
                                        // .sort({completed:1,priority:1,createdAt:1})

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
      const {itemId,desc,amt,cat,date} = req.body;
      // console.log(req.body)
      await TransactionItem.findOneAndUpdate(
        {_id:itemId},
        {$set: {desc,amt,cat,date}} );
      
      const test =
          await TransactionItem.find({_id:itemId})
      console.log(test)
      res.redirect('/transactions')
});

module.exports = router;