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
            res.render('transactions');
});

module.exports = router;