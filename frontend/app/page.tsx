"use client";

import React from 'react';
import { 
  BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, 
  LineChart, Line, AreaChart, Area 
} from 'recharts';
import { 
  TrendingUp, Users, ShoppingCart, AlertTriangle, 
  ArrowUpRight, ArrowDownRight, Package, Loader2
} from 'lucide-react';

const data = [
  { name: 'Mon', actual: 4000, forecast: 4400 },
  { name: 'Tue', actual: 3000, forecast: 3200 },
  { name: 'Wed', actual: 2000, forecast: 2400 },
  { name: 'Thu', actual: 2780, forecast: 2600 },
  { name: 'Fri', actual: 1890, forecast: 2100 },
  { name: 'Sat', actual: 2390, forecast: 2500 },
  { name: 'Sun', actual: 3490, forecast: 3100 },
];

const StatCard = ({ title, value, change, icon: Icon, trend }) => (
  <div className="bg-slate-900/50 backdrop-blur-md border border-slate-800 p-6 rounded-2xl">
    <div className="flex justify-between items-start mb-4">
      <div className="p-2 bg-indigo-500/10 rounded-lg">
        <Icon className="w-6 h-6 text-indigo-400" />
      </div>
      <div className={`flex items-center gap-1 text-sm ${trend === 'up' ? 'text-emerald-400' : 'text-rose-400'}`}>
        {trend === 'up' ? <ArrowUpRight className="w-4 h-4" /> : <ArrowDownRight className="w-4 h-4" />}
        {change}
      </div>
    </div>
    <h3 className="text-slate-400 text-sm font-medium">{title}</h3>
    <p className="text-2xl font-bold text-white mt-1">{value}</p>
  </div>
);

export default function Overview() {
  return (
    <div className="min-h-screen bg-black text-slate-200 p-8 font-sans">
      <div className="max-w-7xl mx-auto">
        <header className="flex justify-between items-end mb-10">
          <div>
            <h1 className="text-4xl font-bold bg-gradient-to-r from-white to-slate-400 bg-clip-text text-transparent">
              Demand Intelligence
            </h1>
            <p className="text-slate-500 mt-2">Enterprise Resource Planning & Forecasting Dashboard</p>
          </div>
          <div className="flex gap-4">
            <button className="px-4 py-2 bg-slate-900 border border-slate-800 rounded-lg text-sm font-medium hover:bg-slate-800 transition-colors">
              Export Report
            </button>
            <button className="px-4 py-2 bg-indigo-600 rounded-lg text-sm font-medium hover:bg-indigo-500 transition-colors whitespace-nowrap">
              Run Retraining
            </button>
          </div>
        </header>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-10">
          <StatCard title="Total SKUs" value="1,284" change="+12%" icon={Package} trend="up" />
          <StatCard title="Forecast Accuracy" value="94.2%" change="+2.4%" icon={TrendingUp} trend="up" />
          <StatCard title="At-Risk SKUs" value="42" change="-18%" icon={AlertTriangle} trend="down" />
          <StatCard title="Missed Sales (Est)" value="$12.4k" change="-5.2%" icon={ShoppingCart} trend="down" />
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          <div className="lg:col-span-2 bg-slate-900/40 backdrop-blur-sm border border-slate-800 p-8 rounded-3xl">
            <div className="flex justify-between items-center mb-8">
              <h2 className="text-xl font-semibold">Demand Projection vs Actual</h2>
              <select className="bg-slate-950 border border-slate-800 rounded-md px-3 py-1 text-xs">
                <option>Last 7 Days</option>
                <option>Last 30 Days</option>
              </select>
            </div>
            <div className="h-80 w-full">
              <ResponsiveContainer width="100%" height="100%">
                <AreaChart data={data}>
                  <defs>
                    <linearGradient id="colorActual" x1="0" y1="0" x2="0" y2="1">
                      <stop offset="5%" stopColor="#6366f1" stopOpacity={0.3}/>
                      <stop offset="95%" stopColor="#6366f1" stopOpacity={0}/>
                    </linearGradient>
                  </defs>
                  <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" vertical={false} />
                  <XAxis dataKey="name" stroke="#64748b" fontSize={12} tickLine={false} axisLine={false} />
                  <YAxis stroke="#64748b" fontSize={12} tickLine={false} axisLine={false} />
                  <Tooltip 
                    contentStyle={{ backgroundColor: '#0f172a', border: '1px solid #1e293b', borderRadius: '12px' }}
                    itemStyle={{ color: '#fff' }}
                  />
                  <Area type="monotone" dataKey="actual" stroke="#6366f1" strokeWidth={3} fillOpacity={1} fill="url(#colorActual)" />
                  <Area type="monotone" dataKey="forecast" stroke="#94a3b8" strokeWidth={2} strokeDasharray="5 5" fill="transparent" />
                </AreaChart>
              </ResponsiveContainer>
            </div>
          </div>

          <div className="bg-slate-900/40 backdrop-blur-sm border border-slate-800 p-8 rounded-3xl">
            <h2 className="text-xl font-semibold mb-8">Stock-out Risk Alert</h2>
            <div className="space-y-6">
              {[
                { id: 'PROD-742', stock: '12 units', risk: 'Critical', color: 'text-rose-400' },
                { id: 'PROD-109', stock: '45 units', risk: 'High', color: 'text-orange-400' },
                { id: 'PROD-221', stock: '89 units', risk: 'Medium', color: 'text-yellow-400' },
                { id: 'PROD-903', stock: '5 units', risk: 'Critical', color: 'text-rose-400' },
              ].map((item) => (
                <div key={item.id} className="flex justify-between items-center group cursor-pointer hover:bg-slate-800/50 p-2 -m-2 rounded-xl transition-all">
                  <div>
                    <p className="text-sm font-medium text-white">{item.id}</p>
                    <p className="text-xs text-slate-500">In stock: {item.stock}</p>
                  </div>
                  <div className={`text-xs font-bold px-3 py-1 bg-slate-950 rounded-full border border-slate-800 ${item.color}`}>
                    {item.risk}
                  </div>
                </div>
              ))}
            </div>
            <button className="w-full mt-10 py-3 bg-indigo-600/10 text-indigo-400 border border-indigo-500/20 rounded-xl text-sm font-bold hover:bg-indigo-600 hover:text-white transition-all">
              View All Alerts
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
