const express = require('express')
const axios = require('axios')

const getAllUserSeries = function (req, res, next){
        //const userCookiesData = req.cookies.data;
        const url = `http://localhost:5000/api/series/user/${req.userCookiesData.userId}`
        axios.get(url).then(response => {

                req.seriesOfUser = response.data
                next()


})
}

module.exports = getAllUserSeries
