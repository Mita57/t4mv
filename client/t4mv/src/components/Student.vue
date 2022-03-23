<template>
    <div v-if="currentStudent" class="edit-form py-3">
        <p class="headline">Edit Student</p>
        <v-form ref="form" lazy-validation>
            <v-text-field
                    v-model="currentStudent.name"
                    :rules="[(v) => !!v || 'Name is required']"
                    label="Name"
                    required
            ></v-text-field>
            <v-text-field
                    v-model="currentStudent.group"
                    :rules="[(v) => !!v || 'Group is required']"
                    label="Group"
                    required
            ></v-text-field>
            <v-text-field
                    v-model="currentStudent.year"
                    :rules="[(v) => !!v || 'Year is required']"
                    label="Year"
                    required
            ></v-text-field>
            <v-btn color="error" small class="mr-2" @click="deleteStudent">
                Delete
            </v-btn>
            <v-btn color="primary" small class=" mr-3" to="/">Back</v-btn>
        </v-form>
        <p class="mt-3">{{ message }}</p>
    </div>
    <div v-else>
        <p>Please click on a Student...</p>
    </div>
</template>
<script>
    import StudentsDataService from "../services/StudentsDataService";
    export default {
        name: "tutorial",
        data() {
            return {
                currentStudent: null,
                message: "",
            };
        },
        methods: {
            getStudent(id) {
                StudentsDataService.get(id)
                    .then((response) => {
                        this.currentStudent = response.data;
                        console.log(response.data);
                    })
                    .catch((e) => {
                        console.log(e);
                    });
            },
            deleteStudent() {
                StudentsDataService.delete(this.currentStudent.id)
                    .then((response) => {
                        console.log(response.data);
                        this.$router.push({ name: "tutorials" });
                    })
                    .catch((e) => {
                        console.log(e);
                    });
            },
        },
        mounted() {
            this.message = "";
            this.getStudent(this.$route.params.id);
        },
    };
</script>
<style>
    .edit-form {
        max-width: 300px;
        margin: auto;
    }
</style>
