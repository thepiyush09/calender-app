import React, { useEffect, useState } from 'react';
import axios from 'axios';

const CompanyDashboard = () => {
    const [companies, setCompanies] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:5000/api/companies/')
            .then(response => setCompanies(response.data))
            .catch(error => console.error(error));
    }, []);

    return (
        <div>
            <h1>Company Dashboard</h1>
            <table>
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Location</th>
                        <th>LinkedIn</th>
                        <th>Emails</th>
                        <th>Phone Numbers</th>
                    </tr>
                </thead>
                <tbody>
                    {companies.map(company => (
                        <tr key={company.id}>
                            <td>{company.name}</td>
                            <td>{company.location}</td>
                            <td><a href={company.linkedin}>LinkedIn</a></td>
                            <td>{company.emails}</td>
                            <td>{company.phone_numbers}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default CompanyDashboard;
