const express = require('express'),
	cookieParser = require('cookie-parser'),
	bodyParser = require('body-parser'),
	verifyCookies = require('./middlewares/verifyCookies'),
	getallseries = require('./middlewares/getallseries'),
	cors = require('cors'),
	loginRouter = require('./routes/login'),
	addseriesRouter = require('./routes/addseries'),
	profileRouter = require('./routes/profile'),
	signupRouter = require('./routes/signup')


const app = express();

app.use(cors({ origin: '*' }));

app.use(bodyParser.urlencoded({	extended: true }));
app.use(bodyParser.json());
app.use(cookieParser());

app.use(verifyCookies);

app.use(express.static(__dirname + '/public'));

app.set("view engine", "ejs");

app.use('/login', loginRouter);
app.use('/addseries', addseriesRouter);
app.use('/profile', profileRouter);
app.use('/signup', signupRouter);

app.get('/',getallseries ,(req, res) =>{

        if (req.teste){
		
		res.render('index', {series: req.data, user: req.usercookies.data.user})
	   
	   }else{
		res.render('index', {series: req.data, user: undefined})
		
	   }

});

app.get('/r', (req, res) => {

	res.redirect('/')

} )

app.listen(8000, () => {console.log("Funcionando")});
