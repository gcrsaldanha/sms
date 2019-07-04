import React from "react";
import PropTypes from "prop-types";


const Table = ({ data }) =>
    !data.length ? (
        <p>Nothing to show</p>
    ) : (
        <div className="column">
            <h2 className="subtitle">
                Showing <strong>{ data.length } items</strong>
            </h2>
            <table className="table is-striped">
                <thead>
                <tr>
                    { Object.entries(data[0]).map(entry => <th key={entry[1]}>{entry[0]}</th>) }
                </tr>
                </thead>
                <tbody>
                {data.map(el => (
                    <tr key={el.id}>
                        { Object.entries(el).map(entry => <td key={entry[1]}>{el[1]}</td>) }
                    </tr>
                ))}
                </tbody>
            </table>
        </div>
    );

Table.propTypes = {
    data: PropTypes.array.isRequired
};
export default Table;