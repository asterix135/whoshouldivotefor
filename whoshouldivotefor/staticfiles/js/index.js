var React = require('react');
var ReactDOM = require('react-dom');
var createReactClass = require('create-react-class');

var Welcome = createReactClass({
  render: function(){
    return(
      <h2>
        Welcome to the Playground!
      </h2>
    )
  }
});

var ProvinceSelector = createReactClass({
  render: function(){
    return(
      <input className="form-control" name="province" placeholder="province name"></input>
    )
  }
});

var QuizApp = createReactClass({
  render: function(){
    return (
      <div>
        <h1 className="display-3">
        Where do you live?
        </h1>
        <ProvinceSelector />
      </div>
    )
  }
})

// ReactDOM.render(<Hello />, document.getElementById('container'));
ReactDOM.render(<QuizApp />, document.getElementById('container'));
ReactDOM.render(<Welcome />, document.getElementById('welcome'));
