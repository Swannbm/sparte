import * as L from 'leaflet'
import Tabs from './tabs.js'
import TileLayer from './tile-layer.js'
import GeoJSONLayer from './geojson-layer.js'
import { debounce } from './utils.js'

export default class SparteMap {
    constructor(_options = {}) {
        window.sparteMap = this

        this.targetElement = _options.targetElement
        this.debug = _options.debug
        this.mapCenter = _options.mapCenter
        this.defaultZoom = _options.defaultZoom
        this.layerList = _options.layerList
        this.couv_leafs = _options.couv_leafs
        this.usa_leafs = _options.usa_leafs
        this.projectId = _options.projectId

        if (!this.targetElement) {
            console.warn('Missing \'targetElement\' property')
            return
        }

        this.setConfig()
        this.setTabs()
        this.setMap()
        this.setLayers()

        if (this.debug)
            this.setDebug()
    }

    setDebug() {
        this.debugPanel = document.getElementById("debug-tab")
        this.debugPanel.innerHTML = '<strong>Mode Debug activé</strong>'

        // Display size
        this.debugPanelSize = document.createElement('div')
        this.debugPanelSize.innerHTML = `<strong>Size:</strong> w ${this.config.width} x h ${this.config.height}`
        this.debugPanel.appendChild(this.debugPanelSize)

        // Display bounds
        this.debugPanelBounding = document.createElement('div')
        this.debugPanel.appendChild(this.debugPanelBounding)

        // Display zoom level
        this.debugPanelZoom = document.createElement('div')
        this.debugPanel.appendChild(this.debugPanelZoom)

        // Refresh layers option
        this.debugPanelRefreshLayers = document.createElement('div')

        this.refreshLayersControl = document.createElement('input')
        this.refreshLayersControl.className = 'fr-mr-1w'
        this.refreshLayersControl.type = 'checkbox'
        this.refreshLayersControl.name = 'refresh'
        this.refreshLayersControl.value = 'refresh'
        this.refreshLayersControl.id = 'refresh'
        this.refreshLayersControl.checked = true

        let label = document.createElement('label')
        label.htmlFor = 'Refresh layers'
        label.appendChild(document.createTextNode('refresh'))
        this.debugPanelRefreshLayers.appendChild(this.refreshLayersControl)
        this.debugPanelRefreshLayers.appendChild(label)
        this.debugPanel.appendChild(this.debugPanelRefreshLayers)

        this.refreshLayersControl.addEventListener('change', (_event) => {
            if (_event.target.checked) {
                this.layers.map((_obj) => {
                    _obj.update()
                })
            }
        })

        // Debug events tracking
        this.map.on('moveend', () => {
            this.debugPanelZoom.innerHTML = `<strong>Zoom level:</strong> ${this.map.getZoom()}`
            this.debugPanelBounding.innerHTML = `<strong>Bounds:</strong> SW ${this.map.getBounds().getSouthWest().toString()}, NE ${this.map.getBounds().getNorthEast().toString()}`
        })
    }

    setConfig() {
        this.config = {}

        // Width and height
        const boundings = this.targetElement.getBoundingClientRect()
        this.config.width = boundings.width
        this.config.height = boundings.height || window.innerHeight
    }

    setMap() {
        this.map = L.map(this.targetElement.id, {
            center: this.mapCenter,
            zoom: this.defaultZoom,
            minZoom: 6,
            doubleClickZoom: false,
            attributionControl: false
        })

        // Position zoom control
        // this.map.zoomControl.setPosition('bottomleft')

        // Set max bounds
        let southWest = L.latLng(41.650542, -6.855469),
            northEast = L.latLng(51.830852, 13.359375),
            bounds = L.latLngBounds(southWest, northEast)
        this.map.setMaxBounds(bounds)

        this.map.on('moveend', debounce(() => this.moveend(), 1000))
    }

    setTabs() {
        const tabList = [
            {
                id: 'layer',
                iconClass: 'bi-layers',
                title: 'Options des calques',
            },
            {
                id: 'data',
                iconClass: 'bi-bar-chart',
            }
        ]

        if (this.debug)
            tabList.push(
                {
                    id: 'debug',
                    iconClass: 'bi-bug',
                }
            )

        this.tabs = new Tabs({
            tabList: tabList,
        })
    }

    setLayers() {
        this.layers = []

        this.layerList.map((_obj) => {
            switch (_obj.type) {
                case 'tile':
                    this.layers.push(new TileLayer(_obj))
                    break;
                case 'geojson':
                    this.layers.push(new GeoJSONLayer(_obj))
                    break;
                default:
                    console.log(`Missing layer type for layer ${_obj.name}`);
            }
        })
    }

    moveend() {
        if (this.layers)
            this.layers.map((_obj) => {
                if (this.debug && !this.refreshLayersControl.checked)
                    return

                _obj.update()
            })
    }
}

// Add SparteMap object to the window scope
window.SparteMap = SparteMap
