const express = require('express')


const verifyIfTheresUserCookies = function (req, res, next){
	const userCookiesData = req.cookies;
        if (Object.keys(userCookiesData).length === 0 && userCookiesData.costructor == undefined){
                  req.theresUserCookiesData = false
		  						next()
        }else{
                  req.theresUserCookiesData = true
								  req.userCookiesData = userCookiesData.userData.userData
								  console.log(userCookiesData.userData.userData)
								  next()
        }
};

module.exports = verifyIfTheresUserCookies


