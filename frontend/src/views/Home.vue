<script >
// import TheWelcome from '../components/TheWelcome.vue'
import axios from 'axios'

export default {
    data() {
        return {
            data:[]
        };
    },
    methods: {
        async collect_data() {
            // alert("button clicked")
            try {
                const response = await axios.get('http://127.0.0.1:5000/api/admin/pro'); 
                console.log(response,'response')
                this.data = response.data.pros
                console.log(pros)
            }
            catch (error) {
                console.log(error,'asdfg')
            }
        }
    }
}


// const loaddata = async () => {
    
//     try {
//       const response = await axios.get('http://127.0.0.1:5000/api/admin/pro', {
//         username: username.value,
//         password: password.value
//       })
//       console.log(response,'response')
//       if (response.status === 200) {
//         localStorage.setItem('token', response.data.token) // Save token in localStorage
//         router.push('/')
//       }
//     } catch (err) {
//       error.value = err.response?.data?.message || 'Login failed'
//     }
//   }
  </script>

<template>
    <div>
        <button class="flex_button" @click="collect_data()">
            load data
        </button>
    </div>
   <div>
    <!-- {{ data }} -->
   </div>
  <!-- <div class="panel"> -->
    <div class="table_lebel">

        All Registered Proffessionals</div>
    <!-- <div style=" margin-left: 10%; border-radius: 8px; margin-right: 10%;  padding-bottom: 0.5%; background-color: #fcfeff;"> -->
    <br>
    <table>
        <thead>
            <tr>
                <th>S no.</th>
                <th>Name | Username</th>
                <th>Location</th>
                <th>Date Of Joining </th>
                <th>Service </th>
                <th>Rating</th>
                <th>Status</th>
                <th>Visit</th>
            </tr>
        </thead>
        <tbody>
            
            <tr v-for="(req, index) in data" :key="index">
            <td>{{ index }}</td>
            <td>{{ req.name }} | {{ req.username }}</td>
            <td>{{ req.user_pincode }} || {{ req.user_address }}</td>
            <td>{{ req.user_date }}</td>
            <td>{{ req.user_service }}</td>
            <td>{{ req.user_rating }}</td>
            <td>
                <div v-if="req.user_status === 'reject' || req.user_status === 'ban'" style="color: red;">
                {{ req.user_status }}
                </div>
                <div v-else-if="req.user_status === 'archive'" style="color: rgb(134, 133, 133);">
                Archived
                </div>
                <div v-else-if="req.user_status === 'allow'" style="color: green;">
                Allowed
                </div>
                {{ req.user_role }}
            </td>
            <td style="min-width: 100px;">
                <form @submit.prevent="visit(req.id)">
                <button type="submit">Visit</button>
                </form>
            </td>
            </tr>
        
        </tbody>
     </table>
    <!-- <!-- paginator starts here mj 
    <div class="paginator">

        <div style="justify-content: flex-start; align-items: center;">
            Showing Page {{pros.page}} out of {{pros.pages}}
        </div>
        <div style="justify-content: flex-start;">

            <!-- <div style="display: flex; justify-content: flex-start;"> 
            <div style="justify-content: flex-start;">

                {% if pros.has_prev %}
                <a id="active_pgntr" href="{{ url_for('main.admin_pro', page=pros.prev_num) }}">Previous</a>

                {% else %}
                <a>Previous</a>

                {% endif %}

            </div>

            <div style=" justify-content: center;">
                <form style="display:flex;" action="{{ url_for('main.admin_pro')}}">
                    <input style="width:40px;" id="page_a" name='page' value="{{pros.page}}">
                    <button type="submit"> Go </button>
                </form>
            </div>

            <div style="justify-content: flex-end;">
                {% if pros.has_next %}


                <a id="active_pgntr" href="{{ url_for('main.admin_pro', page=pros.next_num) }}">Next</a>
                {% else %}
                <a>Next</a>

                {% endif %}
            </div>
        </div>
    </div> -->
    <!-- paginator ends here mj   -->
<!-- </div> -->

<!-- <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYtb+B4H3U4QgUilaY4th10TkjB0mJ6cnB4yV0ByFPDKShp2" crossorigin="anonymous"> -->





</template>

