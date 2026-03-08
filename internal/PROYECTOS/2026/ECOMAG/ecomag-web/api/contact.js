/**
 * Contact Form API Endpoint
 * Compatible with Vercel Serverless Functions and Netlify Functions.
 *
 * For Vercel: place this file at /api/contact.js (already done).
 * For Netlify: move to /netlify/functions/contact.js and adjust exports.
 */

const ALLOWED_ORIGIN = 'https://ecomagsas.com';

// ── CORS headers ──
function corsHeaders(origin) {
  const isAllowed = origin === ALLOWED_ORIGIN || origin === 'http://localhost:4321';
  return {
    'Access-Control-Allow-Origin': isAllowed ? origin : ALLOWED_ORIGIN,
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '86400',
  };
}

// ── Validation helpers ──
const EMAIL_REGEX = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
const PHONE_REGEX = /^(\+57\s?)?[0-9\s\-()]{7,15}$/;

function validateBody(body) {
  const errors = [];

  if (!body.nombre || body.nombre.trim().length === 0) {
    errors.push('El nombre es obligatorio.');
  }
  if (!body.telefono || body.telefono.trim().length === 0) {
    errors.push('El telefono es obligatorio.');
  } else if (!PHONE_REGEX.test(body.telefono.trim())) {
    errors.push('Numero de telefono invalido.');
  }
  if (!body.email || body.email.trim().length === 0) {
    errors.push('El email es obligatorio.');
  } else if (!EMAIL_REGEX.test(body.email.trim())) {
    errors.push('Email invalido.');
  }
  if (!body.mensaje || body.mensaje.trim().length === 0) {
    errors.push('El mensaje es obligatorio.');
  } else if (body.mensaje.trim().length < 10) {
    errors.push('El mensaje debe tener al menos 10 caracteres.');
  }

  return errors;
}

// ── Rate Limiting (placeholder) ──
// To implement rate limiting with Vercel KV:
//
// import { kv } from '@vercel/kv';
//
// async function checkRateLimit(ip) {
//   const key = `contact_rate:${ip}`;
//   const count = await kv.incr(key);
//   if (count === 1) await kv.expire(key, 3600); // 1 hour window
//   return count <= 5; // max 5 requests per hour
// }
//
// For Upstash Redis (works on any platform):
// import { Redis } from '@upstash/redis';
// const redis = new Redis({ url: process.env.UPSTASH_REDIS_URL, token: process.env.UPSTASH_REDIS_TOKEN });

// ── reCAPTCHA v3 Verification (placeholder) ──
// async function verifyRecaptcha(token) {
//   const secret = process.env.RECAPTCHA_SECRET_KEY;
//   const res = await fetch('https://www.google.com/recaptcha/api/siteverify', {
//     method: 'POST',
//     headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
//     body: `secret=${secret}&response=${token}`,
//   });
//   const data = await res.json();
//   return data.success && data.score >= 0.5;
// }

// ── Microsoft Graph API Email Sending ──
// Requires Azure AD App Registration with Mail.Send permission.
// See OFFICE365_SETUP.md for full setup instructions.
//
// Environment variables needed:
//   AZURE_TENANT_ID, AZURE_CLIENT_ID, AZURE_CLIENT_SECRET, OFFICE365_SENDER_EMAIL
//
// async function sendEmailViaGraph({ nombre, empresa, telefono, email, mensaje }) {
//   // 1. Get OAuth2 access token
//   const tokenUrl = `https://login.microsoftonline.com/${process.env.AZURE_TENANT_ID}/oauth2/v2.0/token`;
//   const tokenRes = await fetch(tokenUrl, {
//     method: 'POST',
//     headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
//     body: new URLSearchParams({
//       client_id: process.env.AZURE_CLIENT_ID,
//       client_secret: process.env.AZURE_CLIENT_SECRET,
//       scope: 'https://graph.microsoft.com/.default',
//       grant_type: 'client_credentials',
//     }),
//   });
//   const tokenData = await tokenRes.json();
//   const accessToken = tokenData.access_token;
//
//   // 2. Send email via Graph API
//   const senderEmail = process.env.OFFICE365_SENDER_EMAIL;
//   const graphUrl = `https://graph.microsoft.com/v1.0/users/${senderEmail}/sendMail`;
//   const mailRes = await fetch(graphUrl, {
//     method: 'POST',
//     headers: {
//       Authorization: `Bearer ${accessToken}`,
//       'Content-Type': 'application/json',
//     },
//     body: JSON.stringify({
//       message: {
//         subject: `[ECOMAG Web] Nuevo contacto de ${nombre}`,
//         body: {
//           contentType: 'HTML',
//           content: `
//             <h2>Nuevo mensaje de contacto</h2>
//             <table style="border-collapse:collapse;width:100%;max-width:600px;">
//               <tr><td style="padding:8px;font-weight:bold;border-bottom:1px solid #eee;">Nombre:</td><td style="padding:8px;border-bottom:1px solid #eee;">${nombre}</td></tr>
//               <tr><td style="padding:8px;font-weight:bold;border-bottom:1px solid #eee;">Empresa:</td><td style="padding:8px;border-bottom:1px solid #eee;">${empresa || 'No especificada'}</td></tr>
//               <tr><td style="padding:8px;font-weight:bold;border-bottom:1px solid #eee;">Telefono:</td><td style="padding:8px;border-bottom:1px solid #eee;">${telefono}</td></tr>
//               <tr><td style="padding:8px;font-weight:bold;border-bottom:1px solid #eee;">Email:</td><td style="padding:8px;border-bottom:1px solid #eee;"><a href="mailto:${email}">${email}</a></td></tr>
//               <tr><td style="padding:8px;font-weight:bold;vertical-align:top;">Mensaje:</td><td style="padding:8px;">${mensaje.replace(/\n/g, '<br>')}</td></tr>
//             </table>
//           `,
//         },
//         toRecipients: [{ emailAddress: { address: senderEmail } }],
//         replyTo: [{ emailAddress: { address: email, name: nombre } }],
//       },
//       saveToSentItems: true,
//     }),
//   });
//
//   if (!mailRes.ok) {
//     const errBody = await mailRes.text();
//     throw new Error(`Graph API error (${mailRes.status}): ${errBody}`);
//   }
// }

// ── SMTP Alternative (using nodemailer) ──
// npm install nodemailer
//
// import nodemailer from 'nodemailer';
//
// async function sendEmailViaSMTP({ nombre, empresa, telefono, email, mensaje }) {
//   const transporter = nodemailer.createTransport({
//     host: 'smtp.office365.com',
//     port: 587,
//     secure: false,
//     auth: {
//       user: process.env.SMTP_USER,
//       pass: process.env.SMTP_PASS,
//     },
//   });
//
//   await transporter.sendMail({
//     from: process.env.SMTP_USER,
//     to: process.env.SMTP_USER,
//     replyTo: email,
//     subject: `[ECOMAG Web] Nuevo contacto de ${nombre}`,
//     html: `<p><strong>Nombre:</strong> ${nombre}</p>
//            <p><strong>Empresa:</strong> ${empresa || 'N/A'}</p>
//            <p><strong>Telefono:</strong> ${telefono}</p>
//            <p><strong>Email:</strong> ${email}</p>
//            <p><strong>Mensaje:</strong><br>${mensaje.replace(/\n/g, '<br>')}</p>`,
//   });
// }

// ── Handler ──
export default async function handler(req, res) {
  const origin = req.headers.origin || '';
  const headers = corsHeaders(origin);

  // Set CORS headers
  Object.entries(headers).forEach(([key, value]) => res.setHeader(key, value));

  // Handle preflight
  if (req.method === 'OPTIONS') {
    return res.status(204).end();
  }

  // Only allow POST
  if (req.method !== 'POST') {
    return res.status(405).json({ message: 'Metodo no permitido.' });
  }

  try {
    const body = req.body;

    // Honeypot check
    if (body._gotcha) {
      // Silently accept but do nothing (don't reveal bot detection)
      return res.status(200).json({ message: 'Mensaje enviado correctamente.' });
    }

    // Server-side validation
    const errors = validateBody(body);
    if (errors.length > 0) {
      return res.status(422).json({ message: errors[0], errors });
    }

    // Rate limiting check (uncomment when configured)
    // const clientIp = req.headers['x-forwarded-for']?.split(',')[0] || req.socket.remoteAddress;
    // const allowed = await checkRateLimit(clientIp);
    // if (!allowed) {
    //   return res.status(429).json({ message: 'Demasiadas solicitudes. Intente nuevamente en una hora.' });
    // }

    // reCAPTCHA check (uncomment when configured)
    // if (body.recaptchaToken) {
    //   const valid = await verifyRecaptcha(body.recaptchaToken);
    //   if (!valid) {
    //     return res.status(403).json({ message: 'Verificacion de seguridad fallida.' });
    //   }
    // }

    // Send email (uncomment when credentials are configured)
    // await sendEmailViaGraph(body);
    // -- OR --
    // await sendEmailViaSMTP(body);

    // For now: return success (email sending will be enabled when credentials are provided)
    console.log('[Contact Form] New submission:', {
      nombre: body.nombre,
      empresa: body.empresa || 'N/A',
      email: body.email,
      telefono: body.telefono,
      timestamp: new Date().toISOString(),
    });

    return res.status(200).json({ message: 'Mensaje enviado correctamente.' });
  } catch (error) {
    console.error('[Contact Form] Error:', error);
    return res.status(500).json({ message: 'Error interno del servidor. Intente nuevamente.' });
  }
}
