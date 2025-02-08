import { useEffect, useState } from 'react';
  
function DriverPassTypeTwo( DriverLicenseIDIn: { DriverLicenseID: string } ) {

    const [handleStatusWritingExam, setHandleStatusWritingExam] = useState<string>("wait");
    const [handleStatusPracticalExam, setHandleStatusPracticalExam] = useState<string>("wait");
    const [statusNewbieSetIn, setStatusNewbieSetIn] = useState<string>("wait");
    const [exitValue, setExitValue] = useState<string>("wait");

    useEffect(() => {
        if (statusNewbieSetIn === "done") {
            setStatusNewbieSetIn("wait")

            fetch("http://127.0.0.1:5000/change_status_driverLicense", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ driverLicenseID: DriverLicenseIDIn, driverTypeID: 1 }),
            })
            .then(response => response.json())
            .then(data => {
                console.log(data)
            })
            .catch((error) => {
                console.error('Error:', error);
            });
        }

    }, [handleStatusWritingExam, handleStatusPracticalExam, statusNewbieSetIn])

  return (
    <div className="flex flex-row gap-10 items-center justify-center mt-5">
        {
            handleStatusWritingExam === "wait" ? (
                <button
                    className="px-4 py-2 text-white bg-blue-950 rounded-md hover:bg-blue-900 focus:outline-none focus:ring-2 focus:ring-blue-800"       
                    onClick={ () => setHandleStatusWritingExam("doing") }
                    >
                    ทดสอบเขียน
                </button>
            ) : handleStatusWritingExam === "doing" ? (
                <button
                    className="px-4 py-2 text-white bg-blue-950 rounded-md hover:bg-blue-900 focus:outline-none focus:ring-2 focus:ring-blue-800"       
                    onClick={ () => setHandleStatusWritingExam("done") }
                    >
                    สิ้นสุดการสอบเขียน
                </button>
            ) : null
        }
        {
            handleStatusPracticalExam === "wait" ? (
                <button
                    className="px-4 py-2 text-white bg-blue-950 rounded-md hover:bg-blue-900 focus:outline-none focus:ring-2 focus:ring-blue-800"       
                    onClick={ () => setHandleStatusPracticalExam("doing") }
                    >
                    สอบปฏิบัติ
                </button>
            ) : handleStatusPracticalExam === "doing" ? (
                <button
                    className="px-4 py-2 text-white bg-blue-950 rounded-md hover:bg-blue-900 focus:outline-none focus:ring-2 focus:ring-blue-800"       
                    onClick={ () => setHandleStatusPracticalExam("done") }
                    >
                    สิ้นสุดการสอบปฏิบัติ
                </button>
            ) : handleStatusPracticalExam === "done" && handleStatusWritingExam === "done" && statusNewbieSetIn !== "done" && exitValue !== "done" ? (
                <div>
                    <p>การทดสอบเสร็จสิ้นแล้ว</p>
                    <button
                        className="px-4 py-2 text-white bg-blue-950 rounded-md hover:bg-blue-900 focus:outline-none focus:ring-2 focus:ring-blue-800"       
                        onClick={ () => { 
                            setStatusNewbieSetIn("done") 
                            setExitValue("done")
                        }}
                        >
                        กดออก
                    </button>
                </div>
            ) : null
        }   
    </div>
  )
}

export default DriverPassTypeTwo;
