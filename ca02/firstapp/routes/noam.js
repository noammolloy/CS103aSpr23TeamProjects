const express = require('express');
const router = express.Router();
const User = require('../models/User')
const axios = require('axios')

isLoggedIn = (req,res,next) => {
    if (res.locals.loggedIn) {
      next()
    } else {
      res.redirect('/login')
    }
  }

router.get('/noam/',
  isLoggedIn,
  async (req, res, next) => {
            const r = "";
            res.render('noam', {r});
});

router.post('/noam',
  isLoggedIn,
  async (req, res, next) => {
      const prompt = "Make the following variable name dinosaur themed: ".concat(req.body.prompt);
      const response = await axios.post('https://api.openai.com/v1/engines/text-davinci-003/completions', {
        prompt: prompt
      }, {
        headers: {
          'Authorization': `Bearer ${process.env.APIKEY}`,
        },
      });
      const r = response.data.choices[0].text.trim();
      res.render('noam', {r})
});

module.exports = router;