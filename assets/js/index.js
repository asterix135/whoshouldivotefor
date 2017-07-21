var React = require('react');
var ReactDOM = require('react-dom');
var createReactClass = require('create-react-class');

var SELECTLABEL = 'Hello voter! Where do you live?';

var Welcome = createReactClass({
  render: function(){
    return(
      <div>
        <h2>
          Welcome to the Playground!
        </h2>
        <h1>
          Help in determining which municipal candidate is the best match for you
        </h1>
      </div>
    )
  }
});

var ProvinceSelector = createReactClass({
  render: function(){
    return(
      <div className="col-sm-12 col-md-6 col-lg-4">
        <label className="form-control-label" for="province">{this.props.selectLabel}</label>
        <select className="form-control" name="province" placeholder="province name">
          <option value selected="selected">----------------</option>
          <option value="AB">Alberta</option>
          <option value="BC">British Columbia</option>
          <option value="MB">Manitoba</option>
          <option value="NB">New Brunswick</option>
          <option value="NL">Newfoundland and Labrador</option>
          <option value="NT">Northwest Territories</option>
          <option value="NS">Nova Scotia</option>
          <option value="NU">Nunavut</option>
          <option value="ON">Ontario</option>
          <option value="PE">Prince Edward Island</option>
          <option value="QC">Québec</option>
          <option value="SK">Saskatchewan</option>
          <option value="YK">Yukon</option>
        </select>
      </div>
    )
  }
});


import Main from'./core/containers/main';


// ReactDOM.render(<Hello />, document.getElementById('container'));
// ReactDOM.render(<QuizApp selectLabel={SELECTLABEL}/>, document.getElementById('container'));
// ReactDOM.render(<ButtonApp text={BUTTONTEXT} />, document.getElementById('container'));
ReactDOM.render(<Main />, document.getElementById('welcome'));
// ReactDOM.render(<Game />, document.getElementById('tutorial'))
