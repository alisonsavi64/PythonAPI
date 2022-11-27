const express = require('express')
const axios = require('axios')
const router = express.Router()
const getAllUserSeries = require('../middlewares/getAllUserSeries')

router.get('/', getAllUserSeries ,(req, res) =>{

	res.render("profile", {seriesDataOfUser: req.seriesOfUser, userData: req.userCookiesData})

});

router.delete('/:uniqueid', (req, res) => {
	const specificUniqueIdSerieToDelete = req.params.uniqueid
	const url = `http://localhost:5000/api/series/${specificUniqueIdSerieToDelete}`
	axios.delete(url).then(response => {

		res.redirect('/profile')

	})
	
})

module.exports = router



