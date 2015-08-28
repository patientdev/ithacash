module.exports = {
    options: {
        banner: '/*! <%= pkg.name %>.js <%= grunt.template.today("yyyy-mm-dd") %> */\n'
    },
    global: {
        files: {
            '<%= globalConfig.src  %>/js/patient.js': ['js/patient.dev.js']
        }
    }
};