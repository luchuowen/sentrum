<script>
/* Shared controller: highlights building parts + accumulates the signal path for the active step. */
window.SentrumSteps=function(root){
  const order=['uplink','backbone','core','security','rooms','steel'];
  const parts=[...root.querySelectorAll('.part')],sigs=[...root.querySelectorAll('.sig')],steps=[...root.querySelectorAll('.step')],tabs=[...root.querySelectorAll('[data-go]')];
  let cur=-1;
  function set(k){const i=order.indexOf(k);if(i===cur)return;cur=i;
    parts.forEach(p=>p.classList.toggle('on',p.dataset.step===k));
    sigs.forEach(s=>{const j=order.indexOf(s.dataset.step);s.classList.toggle('done',j>-1&&j<i);s.classList.toggle('live',j===i);});
    steps.forEach(s=>s.classList.toggle('on',s.dataset.step===k));
    tabs.forEach(t=>{const on=t.dataset.go===k;t.setAttribute('aria-selected',on);t.classList.toggle('on',on)});
    root.dispatchEvent(new CustomEvent('step',{detail:{k,i}}));}
  function all(){cur=-1;parts.forEach(p=>p.classList.remove('on'));steps.forEach(s=>s.classList.remove('on'));tabs.forEach(t=>{t.setAttribute('aria-selected','false');t.classList.remove('on')});sigs.forEach(s=>{s.classList.remove('done');s.classList.add('live')});root.dispatchEvent(new CustomEvent('step',{detail:{k:null,i:-1}}));}
  return {order,set,all,get i(){return cur}};
};
</script>
