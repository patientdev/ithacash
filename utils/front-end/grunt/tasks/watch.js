module.exports = {
    options: {
        livereload: true
    },
    css: {
        files: ["scss/*.scss", "<%= django.static %>/../../templates/style-guide.html"],
        tasks: ["sass", "autoprefixer"]
    },
    js: {
        files: ["js/*.js"],
        tasks: ["uglify"]
    }
};
