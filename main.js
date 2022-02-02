const url = "http://127.0.0.1:5000";
var app = new Vue({
  el: "#app",
  data: {
    message: "Hello Vue!",
    items: [],
    name: "",
  },
  async mounted() {
    this.getData();
    // call user
    this.getUser();
  },
  methods: {
    getData: async function () {
      try {
        // fetch data json url

        const rs = await fetch(url + "/companies");
        const data = await rs.json();
        this.items = data;
        console.log(data);
      } catch (error) {
        console.log(error);
      }
    },
    addItem() {
      this.items.push({ id: this.items.length + 1, name: this.name });
    },
    getUser: async function () {
      try {
        // req user
        const rs = await fetch(url + "/users");
        const data = await rs.json();
        console.log(data);
      } catch (error) {}
    },
  },
});
