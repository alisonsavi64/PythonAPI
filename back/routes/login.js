const express = require('express');
const router = express.Router();
const axios = require('axios')

router.get('/', (req, res) =>{

        res.render("login", {user: 'undefined'})
});

router.get('/logout', (req, res) =>{
	res.clearCookie('data')
	res.redirect('/')
})

router.post('/', (req, res) => {

        data = {
                "email": req.body.email,
                "password": req.body.password
        }

        axios.post('http://localhost:5000/api/user/login', {
        data,
        }).then(response => {
                if (Object.keys(response.data).length === 0 && response.data.coo){
			res.send('Login inválido')
                }else{
                        res.cookie('data', response.data)
                        res.redirect(302, '/')
                }
        }).catch((err) => {console.log(err)})

});

module.exports = router
