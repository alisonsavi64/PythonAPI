const express = require('express')
const axios = require('axios')
const router = express.Router()
const getalluserseries = require('../middlewares/getalluserseries')

router.get('/', getalluserseries ,(req, res) =>{
	res.render("profile", {series: req.series, user: req.cookies.data.user})
});

router.delete('/deleteserie/:uniqueid', (req, res) => {
	const id = req.params.uniqueid
	const url = `http://localhost:5000/api/series/delseries/${id}`
	axios.delete(url).then(response => {

		res.redirect('/profile')
	})
	
})

module.exports = router



