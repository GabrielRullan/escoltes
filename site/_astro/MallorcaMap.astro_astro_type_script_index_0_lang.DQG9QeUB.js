import{t as e}from"./rolldown-runtime.D9-fqq9M.js";var t=e((()=>{function e(){let e=document.getElementById(`osmGeneralMap`);if(!e||!window.L||e._leaflet_id)return;let t=window.L,n=JSON.parse(e.dataset.routes||`[]`),r=JSON.parse(e.dataset.acampades||`[]`),i=e.dataset.initialType||`all`,a=[39.6953,2.95],o=window.innerWidth<640?9:10,s=t.map(`osmGeneralMap`,{center:a,zoom:o,scrollWheelZoom:!1});t.tileLayer(`https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png`,{attribution:`&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>`,maxZoom:18}).addTo(s);let c=t.divIcon({className:`osm-custom-pin-route`,html:`<div style="background-color: #1b4332; width: 22px; height: 22px; border-radius: 50%; border: 2.5px solid white; box-shadow: 0 2px 5px rgba(0,0,0,0.3); display: flex; align-items: center; justify-content: center; font-size: 11px; color: white;">🥾</div>`,iconSize:[22,22],iconAnchor:[11,11],popupAnchor:[0,-11]}),l=t.divIcon({className:`osm-custom-pin-camp`,html:`<div style="background-color: #d97706; width: 22px; height: 22px; border-radius: 50%; border: 2.5px solid white; box-shadow: 0 2px 5px rgba(0,0,0,0.3); display: flex; align-items: center; justify-content: center; font-size: 11px; color: white;">🏕️</div>`,iconSize:[22,22],iconAnchor:[11,11],popupAnchor:[0,-11]}),u=[],d=[];n.forEach(e=>{if(!e.lat||!e.lon)return;let n=`
        <div style="font-family: inherit; font-size: 12px; max-width: 240px; padding: 2px;">
          <div style="display: flex; align-items: center; justify-content: space-between; gap: 4px; margin-bottom: 4px;">
            <span style="background: #1b4332; color: white; padding: 2px 6px; border-radius: 4px; font-weight: bold; font-size: 10px;">RUTA</span>
            <span style="color: #666; font-size: 11px;">${e.municipi}</span>
          </div>
          <strong style="font-size: 13px; line-height: 1.3; color: #1c1917; display: block; margin-bottom: 6px;">
            ${e.nom}
          </strong>
          <div style="background: #f5f5f4; padding: 4px 6px; border-radius: 6px; margin-bottom: 6px; display: flex; justify-content: space-between; font-weight: 600; color: #44403c;">
            <span>🥾 ${e.distancia_km} km</span>
            <span>⛰️ +${e.desnivell_positiu_m}m</span>
            <span>${e.dificultat}</span>
          </div>
          <a href="/rutes/${e.slug}" style="display: block; text-align: center; background: #1b4332; color: white; padding: 5px 8px; border-radius: 6px; text-decoration: none; font-weight: bold; margin-top: 6px;">
            Veure fitxa de la ruta →
          </a>
        </div>
      `,r=t.marker([e.lat,e.lon],{icon:c}).bindPopup(n);u.push(r)}),r.forEach(e=>{if(!e.lat||!e.lon)return;let n=`
        <div style="font-family: inherit; font-size: 12px; max-width: 240px; padding: 2px;">
          <div style="display: flex; align-items: center; justify-content: space-between; gap: 4px; margin-bottom: 4px;">
            <span style="background: #d97706; color: white; padding: 2px 6px; border-radius: 4px; font-weight: bold; font-size: 10px;">ACAMPADA / REFUGI</span>
            <span style="color: #666; font-size: 11px;">${e.municipi}</span>
          </div>
          <strong style="font-size: 13px; line-height: 1.3; color: #1c1917; display: block; margin-bottom: 6px;">
            ${e.nom}
          </strong>
          <div style="background: #fef3c7; color: #92400e; padding: 4px 6px; border-radius: 6px; margin-bottom: 6px; font-weight: 600; font-size: 11px;">
            Titularitat: ${e.titularitat}
            ${e.capacitat?`<br>Capacitat: ${e.capacitat}`:``}
          </div>
          ${e.web?`
            <a href="${e.web}" target="_blank" rel="noopener noreferrer" style="display: block; text-align: center; background: #d97706; color: white; padding: 5px 8px; border-radius: 6px; text-decoration: none; font-weight: bold;">
              Web oficial / Reserva ↗
            </a>
          `:`
            <a href="/acampada" style="display: block; text-align: center; background: #57534e; color: white; padding: 5px 8px; border-radius: 6px; text-decoration: none; font-weight: bold;">
              Veure directori d'acampada →
            </a>
          `}
        </div>
      `,r=t.marker([e.lat,e.lon],{icon:l}).bindPopup(n);d.push(r)});let f=t.layerGroup(u),p=t.layerGroup(d);function m(e){e===`all`?(s.hasLayer(f)||s.addLayer(f),s.hasLayer(p)||s.addLayer(p)):e===`rutes`?(s.hasLayer(f)||s.addLayer(f),s.hasLayer(p)&&s.removeLayer(p)):e===`acampada`&&(s.hasLayer(f)&&s.removeLayer(f),s.hasLayer(p)||s.addLayer(p)),document.querySelectorAll(`.map-filter-btn`).forEach(t=>{let n=t;n.className=n.dataset.filter===e?`map-filter-btn px-3 py-1.5 rounded-lg transition bg-white text-stone-900 shadow-xs font-bold`:`map-filter-btn px-3 py-1.5 rounded-lg transition text-stone-600 hover:text-stone-900 font-medium`})}m(i),document.querySelectorAll(`.map-filter-btn`).forEach(e=>{e.addEventListener(`click`,e=>{m(e.currentTarget.dataset.filter||`all`)})}),document.getElementById(`btnResetMapZoom`)?.addEventListener(`click`,()=>{s.setView(a,o)})}document.addEventListener(`DOMContentLoaded`,e),setTimeout(e,300)}));export default t();