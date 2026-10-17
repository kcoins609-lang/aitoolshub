
(function(){
var root=document.documentElement;
try{var t=localStorage.getItem('theme');if(t)root.setAttribute('data-theme',t);}catch(e){}
document.addEventListener('DOMContentLoaded',function(){
  var tb=document.getElementById('themeBtn');
  if(tb){tb.addEventListener('click',function(){
    var n=root.getAttribute('data-theme')==='dark'?'light':'dark';
    root.setAttribute('data-theme',n);try{localStorage.setItem('theme',n);}catch(e){}
  });}
  var mb=document.getElementById('menuBtn'),nl=document.getElementById('navLinks');
  if(mb&&nl){mb.addEventListener('click',function(){nl.classList.toggle('open');});}
  var q=document.getElementById('q'),cards=document.querySelectorAll('[data-tool]'),chips=document.querySelectorAll('.chip'),empty=document.getElementById('empty');
  if(q&&cards.length){
    var cat='all';
    function apply(){
      var term=q.value.trim().toLowerCase(),shown=0;
      cards.forEach(function(c){
        var ok=(cat==='all'||c.dataset.cat===cat)&&(!term||c.dataset.text.indexOf(term)>-1);
        c.classList.toggle('hidden',!ok);if(ok)shown++;
      });
      if(empty)empty.classList.toggle('hidden',shown>0);
    }
    q.addEventListener('input',apply);
    chips.forEach(function(ch){ch.addEventListener('click',function(){
      chips.forEach(function(x){x.classList.remove('on');});ch.classList.add('on');cat=ch.dataset.cat;apply();
    });});
  }
});
})();
