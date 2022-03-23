<template>
    <v-row align="center" class="list px-3 mx-auto">
        <v-col cols="12" sm="12">
            <v-card class="mx-auto mt-10" tile>
                <v-card-title>Students
                </v-card-title>

                <v-data-table
                        :headers="headers"
                        :items="students"
                        disable-pagination
                        :hide-default-footer="true"
                >
                    <template v-slot:[`item.actions`]="{ item }">
                        <v-icon small class="mr-2" @click="editTutorial(item.id)">mdi-pencil</v-icon>
                        <v-icon small @click="deleteStudent(item.id)">mdi-delete</v-icon>
                    </template>
                </v-data-table>
                <v-card-actions>
                    <v-btn
                            color="blue"
                            to="/add"
                            text
                    >
                        Add
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-col>
    </v-row>
</template>
<script>
    import StudentsDataService from "../services/StudentsDataService";
    export default {
        name: "tutorials-list",
        data() {
            return {
                students: [],
                title: "",
                headers: [
                    { text: "Name", align: "start", sortable: false, value: "name" },
                    { text: "Group", value: "group", sortable: false },
                    { text: "Year", value: "year", sortable: false },
                    { text: "Actions", value: "actions", sortable: false },
                ],
            };
        },
        methods: {
            retrieveStudents() {
                StudentsDataService.getAll()
                    .then((response) => {
                        this.students = response.data.map(this.getDisplayTutorial);
                        console.log(response.data);
                    })
                    .catch((e) => {
                        console.log(e);
                    });
            },
            refreshList() {
                this.retrieveStudents();
            },
            editTutorial(id) {
                this.$router.push({ name: "student-details", params: { id: id } });
            },
            deleteStudent(id) {
                const data = {id: id}
                StudentsDataService.delete(data)
                    .then(() => {
                        this.refreshList();
                    })
                    .catch((e) => {
                        console.log(e);
                    });
            },
            getDisplayTutorial(student) {
                return {
                    id: student.id,
                    name: student.name.length > 30 ? student.name.substr(0, 30) + "..." : student.name,
                    group: student.group.length > 30 ? student.group.substr(0, 30) + "..." : student.group,
                    year: student.year.length > 30 ? student.year.substr(0, 30) + "..." : student.year,
                };
            },
        },
        mounted() {
            this.retrieveStudents();
        },
    };
</script>
<style>
    .list {
        max-width: 750px;
    }
</style>
