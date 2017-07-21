const React = require('react');
const createReactClass = require('create-react-class')

const Main = createReactClass({
  render: function(){
    return(
      <div>
        <h1 className="display-3">
          Who Deserves Your Vote?
        </h1>
        <h3>
          Making sense of local elections
        </h3>
        <p>
          We're here to help Canadians make better sense of local elections.
        </p>
        <p>
          Figure out where you stand on important local issues, and identify
          the candidate or candidates who best reflect your values!
        </p>
      </div>
    )
  }
});

export default Main
