const express = require('express')
const router = express.Router()
const axios = require('axios')

router.get('/'  ,(req, res) =>{

        res.render("signup", {user: 'undefined'})
});

router.post('/', (req, res) => {

        data = {
		"name": req.body.name,
                "email": req.body.email,
                "password": req.body.password
        }

        axios.post('http://localhost:5000/api/user/signup', {
        data,
        }).then(response => {
                if (Object.keys(response.data).length === 0){
			res.send('Email já usado')
                }else{
                        res.cookie('data', response.data)
                        res.redirect(302, '/')
                }
        }).catch((err) => {console.log(err)})

});

module.exports = router
