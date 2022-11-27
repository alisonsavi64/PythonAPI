const express = require('express');
const router = express.Router();
const axios = require('axios')

router.get('/', (req, res) =>{

        res.render("login", {userData: undefined})
});

router.get('/logout', (req, res) =>{
	res.clearCookie('userData')
	res.redirect('/')
})

router.post('/', (req, res) => {

        loginUserData = {

                "userEmail": req.body.userEmail,
                "userPassword": req.body.userPassword

        }

        axios.post('http://localhost:5000/api/user/login', {
        loginUserData,
        }).then(response => {
                if (Object.keys(response.data).length === 0){
			res.send('Login inválido')
                }else{
                        res.cookie('userData', response.data)
                        res.redirect(302, '/')
                }
        }).catch((err) => {console.log(err)})

});

module.exports = router
