var dagcomponentfuncs = (window.dashAgGridComponentFunctions =
  window.dashAgGridComponentFunctions || {});

dagcomponentfuncs.ModelLink = function (props) {
  return React.createElement(
    "a",
    { href: "/model/" + props.value },
    props.value
  );
};

dagcomponentfuncs.DatasetLink = function (props) {
  return React.createElement(
    "a",
    { href: "/dataset/" + props.value },
    props.value
  );
};
