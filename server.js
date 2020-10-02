const express = require('express');
const app = express();
app.listen(3000,'127.0.0.1',()=> console.log('listening at 3000'));
app.use(express.static('public'));
app.use(express.json({limit: '1mb'}));
app.use(express.urlencoded({ extended: false }));
app.use(express.raw());
var password = "udith69";
var username = "udith";

app.post('/register',(request, response) =>{

    username = request.body["username"];
    password = request.body["password"];
    console.log(username,password);

});

app.post('/login',(request, response) =>{
    console.log(request.body);
    if(username == request.body.username && password == request.body.password)
    {console.log("cracked");
    response.send({
        'success':true
    });}
    else{
        response.send({
            'success':false
        });
    }

});
