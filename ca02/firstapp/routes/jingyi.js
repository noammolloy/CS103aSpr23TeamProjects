const express = require('express');
const router = express.Router();
const User = require('../models/User')

isLoggedIn = (req,res,next) => {
    if (res.locals.loggedIn) {
      next()
    } else {
      res.redirect('/login')
    }
  }

router.get('/jingyi/',
  isLoggedIn,
  async (req, res, next) => {
            res.render('jingyi');
});

module.exports = router;