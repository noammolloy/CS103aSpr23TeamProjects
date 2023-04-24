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
                                        .sort({completed:1,priority:1,createdAt:1})

      res.render('transactions', items);
});

/* add the value in the body to the list associated to the key */
router.post('/transactions',
  isLoggedIn,
  async (req, res, next) => {
      const transaction = new TransactionItem(
        {description: req.body.desc,
         amount: req.body.amt,
         category: req.body.cat,
         date: new Date()
        })
      await transaction.save();
      res.redirect('/transactions')
});

module.exports = router;