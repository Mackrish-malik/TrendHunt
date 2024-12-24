import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
    const [data, setData] = useState([]);
    const [error, setError] = useState(null);

    useEffect(() => {
        axios.get('http://127.0.0.1:8000/fetch-instagram-data/')
            .then(response => {
                setData(response.data);
            })
            .catch(error => {
                setError('Error fetching data. Please try again later.');
                console.error('Error fetching data:', error);
            });
    }, []);

    return (
        <div className="App">
            <h1>Trending Instagram Posts</h1>
            {error && <p>{error}</p>}
            {data.length === 0 ? (
                <p>Loading...</p>
            ) : (
                data.map((post) => (
                    <div key={post.id}>
                        <img src={post.media_url} alt={post.caption} />
                        <p>{post.caption}</p>
                    </div>
                ))
            )}
        </div>
    );
}

export default App;
