import{t as e}from"./rolldown-runtime.D9-fqq9M.js";var t=e((()=>{var e=null;window.__setMapIsland=function(t){e=t};function t(){let t=document.getElementById(`osmGeneralMap`);if(!t||!window.L||t._leaflet_id)return;let n=window.L,r=JSON.parse(t.dataset.routes||`[]`),i=JSON.parse(t.dataset.acampades||`[]`),a=t.dataset.initialType||`all`,o=[39.5,3],s={mallorca:{center:[39.6953,2.95],zoom:9,bounds:[[39.25,2.3],[39.95,3.5]]},menorca:{center:[39.95,4.1],zoom:10,bounds:[[39.75,3.75],[40.1,4.35]]},eivissa:{center:[38.98,1.4],zoom:10,bounds:[[38.8,1.15],[39.15,1.65]]},formentera:{center:[38.7,1.45],zoom:11,bounds:[[38.6,1.35],[38.8,1.6]]}},c=n.map(`osmGeneralMap`,{center:o,zoom:8,scrollWheelZoom:!1});n.tileLayer(`https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png`,{attribution:`&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>`,maxZoom:18}).addTo(c);let l=n.divIcon({className:`osm-custom-pin-route`,html:`<div style="background-color: #1b4332; width: 22px; height: 22px; border-radius: 50%; border: 2.5px solid white; box-shadow: 0 2px 5px rgba(0,0,0,0.3); display: flex; align-items: center; justify-content: center; font-size: 11px; color: white;">🥾</div>`,iconSize:[22,22],iconAnchor:[11,11],popupAnchor:[0,-11]}),u=n.divIcon({className:`osm-custom-pin-camp`,html:`<div style="background-color: #d97706; width: 22px; height: 22px; border-radius: 50%; border: 2.5px solid white; box-shadow: 0 2px 5px rgba(0,0,0,0.3); display: flex; align-items: center; justify-content: center; font-size: 11px; color: white;">🏕️</div>`,iconSize:[22,22],iconAnchor:[11,11],popupAnchor:[0,-11]}),d=[],f=[];function p(e,t){let n=document.getElementById(`searchInput`),r=document.getElementById(`searchAcampada`),i=document.getElementById(`mapActiveFilterBar`),a=document.getElementById(`mapFilterName`);i&&a&&(i.classList.remove(`hidden`),a.textContent=e),n&&(n.value=e,n.dispatchEvent(new Event(`input`,{bubbles:!0})),document.getElementById(`cercador-rutes`)?.scrollIntoView({behavior:`smooth`,block:`start`})),r&&(r.value=e,r.dispatchEvent(new Event(`input`,{bubbles:!0})),r.scrollIntoView({behavior:`smooth`,block:`center`}))}document.getElementById(`btnClearMapFilter`)?.addEventListener(`click`,()=>{let e=document.getElementById(`mapActiveFilterBar`);e&&e.classList.add(`hidden`);let t=document.getElementById(`resetFilters`);t&&t.click();let n=document.getElementById(`searchAcampada`);n&&(n.value=``,n.dispatchEvent(new Event(`input`,{bubbles:!0})))}),r.forEach(e=>{if(!e.lat||!e.lon)return;let t=`
        <div style="font-family: inherit; font-size: 12px; max-width: 250px; padding: 2px;">
          <div style="display: flex; align-items: center; justify-content: space-between; gap: 4px; margin-bottom: 4px;">
            <span style="background: #1b4332; color: white; padding: 2px 6px; border-radius: 4px; font-weight: bold; font-size: 10px;">RUTA</span>
            <span style="color: #666; font-size: 11px;">${e.municipi} (${e.illa||`Mallorca`})</span>
          </div>
          <strong style="font-size: 13px; line-height: 1.3; color: #1c1917; display: block; margin-bottom: 6px;">
            ${e.nom}
          </strong>
          <div style="background: #f5f5f4; padding: 4px 6px; border-radius: 6px; margin-bottom: 6px; display: flex; justify-content: space-between; font-weight: 600; color: #44403c;">
            <span>🥾 ${e.distancia_km} km</span>
            <span>⛰️ +${e.desnivell_positiu_m}m</span>
            <span>${e.dificultat}</span>
          </div>
          <div style="display: flex; gap: 4px; margin-top: 6px;">
            <button
              type="button"
              onclick="window.__filterMallorca('${e.municipi.replace(/'/g,`\\'`)}')"
              style="flex: 1; text-align: center; background: #e7e5e4; color: #1c1917; padding: 5px 6px; border-radius: 6px; border: none; font-weight: 600; cursor: pointer; font-size: 11px;"
              title="Filtra la llista per aquest municipi"
            >
              🔍 Filtra ${e.municipi}
            </button>
            <a href="/rutes/${e.slug}" style="flex: 1; text-align: center; background: #1b4332; color: white; padding: 5px 6px; border-radius: 6px; text-decoration: none; font-weight: bold; font-size: 11px;">
              Fitxa →
            </a>
          </div>
        </div>
      `,r=n.marker([e.lat,e.lon],{icon:l}).bindPopup(t);r._illa=(e.illa||`Mallorca`).toLowerCase().trim(),r._type=`ruta`,d.push(r)}),i.forEach(e=>{if(!e.lat||!e.lon)return;let t=`
        <div style="font-family: inherit; font-size: 12px; max-width: 250px; padding: 2px;">
          <div style="display: flex; align-items: center; justify-content: space-between; gap: 4px; margin-bottom: 4px;">
            <span style="background: #d97706; color: white; padding: 2px 6px; border-radius: 4px; font-weight: bold; font-size: 10px;">ACAMPADA / REFUGI</span>
            <span style="color: #666; font-size: 11px;">${e.municipi} (${e.illa||`Mallorca`})</span>
          </div>
          <strong style="font-size: 13px; line-height: 1.3; color: #1c1917; display: block; margin-bottom: 6px;">
            ${e.nom}
          </strong>
          <div style="background: #fef3c7; color: #92400e; padding: 4px 6px; border-radius: 6px; margin-bottom: 6px; font-weight: 600; font-size: 11px;">
            Titularitat: ${e.titularitat}
            ${e.capacitat?`<br>Capacitat: ${e.capacitat}`:``}
          </div>
          <div style="display: flex; gap: 4px; margin-top: 6px;">
            <button
              type="button"
              onclick="window.__filterMallorca('${e.municipi.replace(/'/g,`\\'`)}')"
              style="flex: 1; text-align: center; background: #e7e5e4; color: #1c1917; padding: 5px 6px; border-radius: 6px; border: none; font-weight: 600; cursor: pointer; font-size: 11px;"
              title="Filtra la llista per aquest municipi"
            >
              🔍 Filtra ${e.municipi}
            </button>
            ${e.web?`
              <a href="${e.web}" target="_blank" rel="noopener noreferrer" style="flex: 1; text-align: center; background: #d97706; color: white; padding: 5px 6px; border-radius: 6px; text-decoration: none; font-weight: bold; font-size: 11px;">
                Reserva ↗
              </a>
            `:`
              <a href="/acampada" style="flex: 1; text-align: center; background: #57534e; color: white; padding: 5px 6px; border-radius: 6px; text-decoration: none; font-weight: bold; font-size: 11px;">
                Directori →
              </a>
            `}
          </div>
        </div>
      `,r=n.marker([e.lat,e.lon],{icon:u}).bindPopup(t);r._illa=(e.illa||`Mallorca`).toLowerCase().trim(),r._type=`acampada`,f.push(r)}),window.__filterMallorca=e=>{p(e,`municipi`)},window.__filterMap=e=>{p(e,`municipi`)};let m=`all`,h=a;function g(){d.forEach(e=>{let t=h===`all`||h===`rutes`,n=m===`all`||e._illa===m;t&&n?c.hasLayer(e)||c.addLayer(e):c.hasLayer(e)&&c.removeLayer(e)}),f.forEach(e=>{let t=h===`all`||h===`acampada`,n=m===`all`||e._illa===m;t&&n?c.hasLayer(e)||c.addLayer(e):c.hasLayer(e)&&c.removeLayer(e)})}window.__setMapIsland=function(e){let t=(e||``).toLowerCase().trim(),n=t===``||t===`all`||t===`totes`?`all`:t;if(m=n,n===`all`)c.flyTo?c.flyTo(o,8):c.setView(o,8);else{let e=s[n];e&&(e.bounds?c.flyToBounds?c.flyToBounds(e.bounds,{padding:[30,30],maxZoom:12}):c.fitBounds(e.bounds,{padding:[30,30],maxZoom:12}):e.center&&(c.flyTo?c.flyTo(e.center,e.zoom):c.setView(e.center,e.zoom)))}g()};function _(e){h=e,g(),document.querySelectorAll(`.map-filter-btn`).forEach(t=>{let n=t;n.className=n.dataset.filter===e?`map-filter-btn px-3 py-1.5 rounded-lg transition bg-white text-stone-900 shadow-xs font-bold`:`map-filter-btn px-3 py-1.5 rounded-lg transition text-stone-600 hover:text-stone-900 font-medium`})}if(_(a),e)window.__setMapIsland(e),e=null;else try{let e=new URLSearchParams(window.location.search).get(`illa`);e&&window.__setMapIsland(e)}catch{}document.querySelectorAll(`.map-filter-btn`).forEach(e=>{e.addEventListener(`click`,e=>{_(e.currentTarget.dataset.filter||`all`)})}),document.getElementById(`btnResetMapZoom`)?.addEventListener(`click`,()=>{window.__setMapIsland(`all`),window.__setFilterIsland&&window.__setFilterIsland(`all`)})}document.addEventListener(`DOMContentLoaded`,t),setTimeout(t,300)}));export default t();