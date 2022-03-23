import http from "../http-common";
class StudentsDataService {
    getAll() {
        return http.get("/getAll");
    }
    get(id) {
        return http.get(`/getById`, {params: {id: id}});
    }
    create(data) {
        return http.post("/addStudent", data);
    }
    update(id, data) {
        return http.put(`/tutorials/${id}`, data);
    }
    delete(data) {
        return http.delete(`/remove`, {data});
    }
    deleteAll() {
        return http.delete(`/tutorials`);
    }
}
export default new StudentsDataService();
