var mozjpeg = require('imagemin-mozjpeg');
module.exports = {
    dynamic: {
        options: {
            optimizationLevel: 7,
            use: [mozjpeg({quality:80})]
        },
        files: [{
            expand: true,                  // Enable dynamic expansion
            cwd: "img/",                   // Src matches are relative to this path
            src: ["**/*.{png,jpg,gif}"],   // Actual patterns to match
            dest: "<%= django.static %>/img/"                  // Destination path prefix
        }]
    }
};
