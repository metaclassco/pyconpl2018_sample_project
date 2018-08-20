axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";


const productListUrl = Urls["product_list"]();
const productCreateUrl = Urls["product_create"]();


let sampleApp = new Vue({
    el: "#sample_app",
    delimiters: ["[[", "]]"],  // To avoid collisions with Django template delimiters for values
    data: {
        productList: [],

        title: "",
        description: "",
        manufacturer: "",
        category: "",
        formError: "",
    },
    mounted: function () {
        this.loadProductList();
    },
    methods: {
        loadProductList: function() {
            let vm = this;
            axios.get(productListUrl).then(function(response) {
                vm.productList = response.data
            })
        },
        createProduct: function() {
            let vm = this;
            vm.formError = "";
            if (vm.title && vm.description && vm.manufacturer && vm.category) {
                const payload = {
                    "title": vm.title,
                    "description": vm.description,
                    "manufacturer": vm.manufacturer,
                    "category": vm.category,
                };
                axios.post(productCreateUrl, payload).then(function(response) {
                    vm.loadProductList();
                })
            } else {
                vm.formError = "Fields cannot be empty";
            }
        },
        productDelete: function(productId) {
            let vm = this;
            const productDeleteUrl = Urls["product_delete"](productId);
            axios.delete(productDeleteUrl).then(function(response) {
                vm.loadProductList();
            })
        },
    },
});
