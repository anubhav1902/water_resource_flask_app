
document.addEventListener('DOMContentLoaded', function(){
  // Module search
  const search = document.getElementById('search');
  if(search){
    search.addEventListener('input', function(){
      const q = this.value.toLowerCase();
      document.querySelectorAll('.module-card').forEach(c=>{
        c.style.display = c.textContent.toLowerCase().includes(q)?'':'none';
      });
    });
  }

  // Calculator
  const calcBtn = document.getElementById('calcBtn');
  if(calcBtn){
    calcBtn.addEventListener('click', async (e)=>{
      e.preventDefault();
      const liters = Number(document.getElementById('liters').value||0);
      const leaks = Number(document.getElementById('leaks').value||0);
      const households = Number(document.getElementById('households').value||0);
      const resp = await fetch('/calculate', {
        method:'POST',
        headers:{'Content-Type':'application/json'},
        body: JSON.stringify({liters,leaks,households})
      });
      const data = await resp.json();
      document.getElementById('calcResult').textContent = `Estimated yearly water savings: ${data.total} liters`;
      // Draw chart
      const ctx = document.getElementById('calcChart').getContext('2d');
      if(window._chart) window._chart.destroy();
      window._chart = new Chart(ctx, {
        type:'bar',
        data:{
          labels:['Daily','Leaks','Households'],
          datasets:[{label:'Liters',data:[data.liters_saved,data.leaks_saved,data.households_saved],backgroundColor:['#0288d1','#03a9f4','#81d4fa']}]
        }
      });
    });
  }
});
