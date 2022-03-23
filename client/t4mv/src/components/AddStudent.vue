<template>
    <div class="submit-form mt-3 mx-auto">
        <p class="headline">Add Student</p>
        <div v-if="!submitted">
            <v-form ref="form" lazy-validation>
                <v-text-field
                        v-model="student.name"
                        :rules="[(v) => !!v || 'Name is required']"
                        label="Name"
                        required
                ></v-text-field>
                <v-text-field
                        v-model="student.group"
                        :rules="[(v) => !!v || 'Description is required']"
                        label="Group"
                        required
                ></v-text-field>
                <v-text-field
                        v-model="student.year"
                        :rules="[(v) => !!v || 'Year is required']"
                        label="Year"
                        required
                ></v-text-field>
            </v-form>
            <v-btn color="primary" class="mt-3 mr-10" @click="saveStudent">Submit</v-btn>
            <v-btn color="primary" class="mt-3 mr-3" to="/">Back</v-btn>
        </div>
        <div v-else>
            <v-card class="mx-auto">
                <v-card-title>
                    Submitted successfully!
                </v-card-title>
                <v-card-subtitle>
                    Click the button to add new Student or go back to the list.
                </v-card-subtitle>
                <v-card-actions>
                    <v-btn color="success" class="mt-3 mr-10" @click="newStudent">Add</v-btn>
                    <v-btn color="primary" class="mt-3 mr-3" to="/">Back</v-btn>
                </v-card-actions>
            </v-card>
        </div>
    </div>
</template>
<script>
    import StudentsDataService from "../services/StudentsDataService";
    export default {
        name: "add-tutorial",
        data() {
            return {
                student: {
                    id: null,
                    name: "",
                    group: "",
                    year: "2022",
                    published: false,
                },
                submitted: false,
            };
        },
        methods: {
            saveStudent() {
                var data = {
                    name: this.student.name,
                    group: this.student.group,
                    year: this.student.year
                };
                StudentsDataService.create(data)
                    .then((response) => {
                        this.student.id = response.data.id;
                        console.log(response.data);
                        this.submitted = true;
                    })
                    .catch((e) => {
                        console.log(e);
                    });
            },
            newStudent() {
                this.submitted = false;
                this.student = {};
            },
        },
    };
</script>
<style>
    .submit-form {
        max-width: 300px;
    }
</style>
