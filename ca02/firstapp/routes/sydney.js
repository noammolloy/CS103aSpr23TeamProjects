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

router.get('/sydney/',
  isLoggedIn,
  async (req, res, next) => {
            const r = "";
            res.render('sydney', {r});
});

router.post('/sydney',
  isLoggedIn,
  async (req, res, next) => {
      const prompt = "Create a short story using these input keywords about dinosaurs: ".concat(req.body.prompt);
      const response = await axios.post('https://api.openai.com/v1/engines/davinci/completions', {
        prompt: prompt,
        max_tokens: 60,
        n: 1,
        stop: '###',
      }, {
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${process.env.APIKEY}`,
        },
      });
      const r = response.data.choices[0].text.trim();
      console.log(prompt);
      console.log(response)
      console.log(r)
      res.render('sydney', {r})
});

module.exports = router;