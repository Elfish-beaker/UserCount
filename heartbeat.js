export default async function handler(req, res) {
    if (req.method !== "POST") {
        return res.status(405).json({ error: "Method Not Allowed" });
    }

    const { username, target, featureUsed, timestamp } = req.body;

    if (!username || !featureUsed) {
        return res.status(400).json({ error: "Missing required fields" });
    }

    // Example: Save data to Vercel Logs (Temporary Storage)
    console.log("Tracking Data:", { username, target, featureUsed, timestamp });

    return res.status(200).json({ message: "Data logged successfully" });
}
