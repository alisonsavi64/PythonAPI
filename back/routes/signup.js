const express = require('express')
const router = express.Router()
const axios = require('axios')

router.get('/'  ,(req, res) =>{

        res.render("signup", {userData: undefined})
});

router.post('/', (req, res) => {

        signupUserData = {
		"userName": req.body.userName,
                "userEmail": req.body.userEmail,
                "userPassword": req.body.userPassword
        }

        axios.post('http://localhost:5000/api/user/signup', {
        signupUserData,
        }).then(response => {
                if (Object.keys(response.data).length === 0){
			res.send('Email já usado')
                }else{
                        res.cookie('userData', response.data)
                        res.redirect(302, '/')
                }
        }).catch((err) => {console.log(err)})

});

module.exports = router
