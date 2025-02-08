import React, { useEffect, useState } from 'react';

const ReportDriverTypeNumber: React.FC = () => {

    const [data, setData] = useState<[number, string, number][]>([]);

    useEffect(() => {
        fetch("http://127.0.0.1:5000/get_report_driver_type", {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            },
        })
        .then(response => response.json())
        .then(data => {
            if (Array.isArray(data)) {
                setData(data);
            } else {
                console.error("Fetched data is not an array:", data);
            }
        })
        .catch(error => {
            console.error("Error fetching data:", error);
        });
    }, [])

    useEffect(() => {
        console.log("Update State: ", data)
    }, [data])

    return (
        <div className="text-white absolute top-2 left-2">
            <h1>รายงานจำนวนผู้ขับขี่ของประเภทต่างๆ</h1>
            { data && data.map ? (
                data.map((item: any) => (
                    <div key={item[0]}>
                        <p>ประเภท: {item[1] || "N/A"}</p>
                        <p>จำนวน: {item[2] || "N/A"}</p>
                    </div>
                ))
             ) : null }
        </div>
    )
}

export default ReportDriverTypeNumber;