const express = require('express')


const verifyCookies = function (req, res, next){
	const ucookies = req.cookies;
        if (Object.keys(ucookies).length === 0 && ucookies.costructor == undefined){
                  req.teste = false
		  next()
        }else{
                  req.teste = true
		  req.usercookies = ucookies
		  next()
        }
};

module.exports = verifyCookies


