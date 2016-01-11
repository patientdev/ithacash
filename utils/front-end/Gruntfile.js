module.exports = function(grunt) {

  var path = require("path");

  // Grunt configs in grunt/ directory
  require("load-grunt-config")(grunt, {

    configPath: [
      path.join(process.cwd(), "grunt"),
      path.join(process.cwd(), "grunt/tasks")
    ],

    init: true,

    data: {
      django: {
<<<<<<< HEAD
        static: "../../ithacash/static"
=======
        static: "../../ithacash_dev/static"
>>>>>>> refs/remotes/origin/master
      }
    },

    loadGruntTasks: {
        pattern: "grunt-*",
        config: require("./package.json"),
        scope: "devDependencies"
    }

  });
};
