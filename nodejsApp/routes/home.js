const express = require('express')
const getAllSeriesData = require('../middlewares/getAllSeriesData')
const router = express.Router()

router.get('/', getAllSeriesData ,(req, res) =>{
        if (req.theresUserCookiesData){

		res.render('index', {seriesData: req.allSeriesData, userData: req.userCookiesData})
	   
	   }else{

		res.render('index', {seriesData: req.allSeriesData, userData: undefined})
		
	   }

});

module.exports = router