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

router.get('/jingyi/',
  isLoggedIn,
  async (req, res, next) => {
            const r = "";
            res.render('jingyi', {r});
});

router.post('/jingyi',
  isLoggedIn,
  async (req, res, next) => {
      const prompt = "Change the following text to be written as if you are talking to a dinosaur: ".concat(req.body.prompt);
      const response = await axios.post('https://api.openai.com/v1/engines/text-davinci-003/completions', {
        prompt: prompt,
        max_tokens: 3900,
        
      }, {
        headers: {
          'Authorization': `Bearer ${process.env.APIKEY}`,
        },
      });
      const r = response.data.choices[0].text.trim();
      res.render('jingyi', {r})
});

module.exports = router;