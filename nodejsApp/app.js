const express = require('express'),
	cookieParser = require('cookie-parser'),
	bodyParser = require('body-parser'),
	verifyCookies = require('./middlewares/verifyCookies'),
	cors = require('cors'),
	loginRouter = require('./routes/login'),
	addseriesRouter = require('./routes/addseries'),
	profileRouter = require('./routes/profile'),
	signupRouter = require('./routes/signup')
	homeRouter = require('./routes/home')


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
app.use('/', homeRouter);

app.listen(8000, () => {console.log("Funcionando")});
