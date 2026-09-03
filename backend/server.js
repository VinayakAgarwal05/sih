import express from 'express';
import cors from 'cors';
import helmet from 'helmet';
import morgan from 'morgan';
import rateLimit from 'express-rate-limit';
const app=express();
app.use(helmet()); app.use(cors()); app.use(express.json({limit:'1mb'})); app.use(morgan('tiny'));
app.use(rateLimit({windowMs:60_000,max:120}));
const people=[
{id:'P-1042',unit:'Alpha',risk:88,level:'HIGH',persistence:6,trend:'Increasing'},
{id:'P-1192',unit:'Bravo',risk:84,level:'HIGH',persistence:5,trend:'Increasing'},
{id:'P-0873',unit:'Charlie',risk:73,level:'ELEVATED',persistence:3,trend:'Increasing'},
{id:'P-2011',unit:'Alpha',risk:48,level:'MODERATE',persistence:0,trend:'Stable'},
{id:'P-2304',unit:'Delta',risk:29,level:'LOW',persistence:0,trend:'Improving'}];
app.get('/api/health',(req,res)=>res.json({ok:true,service:'SAARTHI AI backend'}));
app.get('/api/personnel',(req,res)=>res.json({data:people,source:'synthetic'}));
app.get('/api/personnel/:id',(req,res)=>{const p=people.find(x=>x.id===req.params.id); if(!p)return res.status(404).json({error:'Not found'}); res.json({data:p});});
app.post('/api/welfare-reviews',(req,res)=>res.status(201).json({ok:true,reviewId:'WR-'+Date.now(),status:'created',message:'Human welfare review created in demo mode.'}));
app.get('/api/audit',(req,res)=>res.json({data:[{time:new Date().toISOString(),actor:'demo',action:'API health/read'}]}));
app.listen(4000,()=>console.log('SAARTHI backend listening on http://localhost:4000'));
