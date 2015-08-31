module.exports = {
    options: {
        banner: '/*! <%= package.name %>.js <%= grunt.template.today("yyyy-mm-dd") %> */\n'
    },
    global: {
        files: {
            '<%= django.static  %>/js/ithacash.js': ['js/*.js']
        }
    }
};
