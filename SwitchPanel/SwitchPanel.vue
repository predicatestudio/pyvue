<template>
    <!-- <div class="hello">Hello {{who}}</div> -->
    <div class="container" id="panel">
        <div class="row">
            <div class="col-xs-12 col-sm-6 col-md-4 col-sm-offset-3 col-md-offset-4">
                <div class="card" style="width: 18rem;">
                    <!-- Default panel contents -->
                    <div class="card-header"> {{ title }} </div>
                    <!-- List group -->
                    <ul class="list-group">
                        <div v-for="switchLine in switches">
                            <Switch :label=switchLine.label :color=switchLine.color />
                        </div>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import Switch from './components/Switch.vue'

export default {
  name: 'SwitchPanel',
  title: 'Material Design Switch Demos',
  components: {
      Switch
  },
  props: {
        title: {
            type: String,
            default: 'Toggle Panel'
        },
        switches: {
            type: Array,
            default: [
            {},
            {
                "label": "Primary Switch",
                "color": "primary"
            },
            {
                "label": "Success Switch",
                "color": "success"
            },    {
                "label": "Info Switch",
                "color": "info"
            },    {
                "label": "Warning Switch",
                "color": "warning"
            },    {
                "label": "Danger Switch",
                "color": "danger"
            }
            
        ]
        }
    }
}
</script>
