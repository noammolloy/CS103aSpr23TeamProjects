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
      console.log(r)
      res.render('jingyi', {r})
});

function clean(str) {
  const index = str.indexOf('\n');
  if (index === -1) {
    return null; // return null if no newline is found
  }
  return str.slice(index + 1);
}

module.exports = router;