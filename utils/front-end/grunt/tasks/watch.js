module.exports = {
    options: {
        livereload: true
    },
    css: {
        files: ["scss/*.scss", "js/*.js", "<%= django.static %>/../../templates/style-guide.html"],
        tasks: ["sass", "autoprefixer", "csslint"]
    }
};
